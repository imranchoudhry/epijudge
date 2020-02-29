from test_framework import generic_test


def find_salary_cap(target_payroll, current_salaries):
    # TODO - you fill in here.
    current_salaries.sort()
    uncompressed_salary = 0
    for index, salary in enumerate(current_salaries):
        hyp_target = 0
        hyp_target = uncompressed_salary + (len(current_salaries)-index) * salary
        if hyp_target==target_payroll:
            return salary
        if hyp_target > target_payroll:
            return (target_payroll - (uncompressed_salary))/(len(current_salaries)-index)
        uncompressed_salary += salary
    return -1.0
    """
    potential_caps = []
    for salary in current_salaries:
        hypothetical_cap = salary
        hypothetical_target = 0
        for sal in current_salaries:
            if sal <= hypothetical_cap:
                hypothetical_target += sal
            else:
                hypothetical_target += hypothetical_cap
        potential_caps.append(hypothetical_target)

    #print(potential_caps)
    unadjusted_index = -2
    for i in range(len(potential_caps)):
        if potential_caps[i] >= target_payroll:
            unadjusted_index = i - 1
            break
    if  unadjusted_index==-2:
        return -1
    adjusted_elemt_count = (len(current_salaries) -1) - unadjusted_index
    #print(unadjusted_index)
    return (target_payroll - sum(current_salaries[:unadjusted_index+1]))/adjusted_elemt_count
            

    #return 0.0
    """

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("find_salary_threshold.py",
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
