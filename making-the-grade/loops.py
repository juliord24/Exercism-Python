"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores : list):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    int_scores_list = list()
    while student_scores:
        int_scores_list.append(round(student_scores.pop()))
    return int_scores_list


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    failed_students_count = 0
    for score in student_scores:
        if score <= 40:
            failed_students_count += 1
    return failed_students_count

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    above_threshold_list = list()
    for score in student_scores:
        if score >= threshold:
            above_threshold_list.append(score)
    return above_threshold_list

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    interval_for_each_letter = (highest - 40) // 4
    lower_score_list = list()
    for i in range(41, highest, interval_for_each_letter):
        lower_score_list.append(i)
    return lower_score_list


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    student_ranking_list = list()
    for index, (score, name) in enumerate(zip(student_scores, student_names)):
        student_ranking_list.append(f"{index + 1}. {name}: {score}")
        
    return student_ranking_list   


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    perfect_score_student = list()
    for student in student_info:
        if student[1] == 100:
            perfect_score_student.append(student[0])
            perfect_score_student.append(student[1])

            break
    return perfect_score_student
