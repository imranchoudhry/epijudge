import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Person = collections.namedtuple('Person', ('age', 'name'))


def group_by_age(people):
    # TODO - you fill in here.
    
    elt_count = len(people)
    t = {}
    for person in people:
        if person.age in t:
            t[person.age] +=1
        else:
            t[person.age] = 1
    nxt = {}
    count = 0
    for age in t:
        nxt[age] = count
        count += t[age]
    print(t)
    print(nxt)

    while nxt:
        age = next(iter(nxt))
        indx = nxt[age]
        curr_person = people[indx]
        swap_index = nxt[curr_person.age]
        people[swap_index], people[indx] = people[indx], people[swap_index]
        """
        print("HELLLO")
        print(f"curr_person.age is {curr_person.age}")
        print(f"indx is {indx}")
        print(f"swap_index is {swap_index}")

        print(people)
        """
        nxt[curr_person.age] =  nxt[curr_person.age] + 1
        t[curr_person.age] = t[curr_person.age] - 1
        if t[curr_person.age] == 0:
            del nxt[curr_person.age]


            
    """
    age_to_count = collections.Counter((person.age for person in people))
    age_to_offset, offset = {}, 0
    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count
    print(age_to_offset)
    """
    """
    for person in people:
        index = nxt[person.age]
        result[index] = person
        nxt[person.age]= index +1
    """
    #print(result)
    return


@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure('Empty result')

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure('Entry set changed')

    ages = set()
    last_age = people[0]

    for x in people:
        if x.age in ages:
            raise TestFailure('Entries are not grouped by age')
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("group_equal_entries.py",
                                       'group_equal_entries.tsv',
                                       group_by_age_wrapper))
