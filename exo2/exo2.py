"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""
def solution(string, ending):
    return string.endswith(ending)

def run_tests():
    fixed_tests_True = (
        ("samurai", "ai"),
        ("ninja", "ja"),
        ("sensei", "i"),
        ("abc", "abc"),
        ("abcabc", "bc"),
        ("fails", "ails")
    )

    fixed_tests_False = (
        ("sumo", "omo"),
        ("samurai", "ra"),
        ("abc", "abcd"),
        ("ails", "fails"),
        ("this", "fails"),
        ("spam", "eggs")
    )

    # Tests True
    for string, ending in fixed_tests_True:
        result = solution(string, ending)
        print(f"Testing if '{string}' ends with '{ending}': {result}")
        assert result == True, f"Test failed for: {string}, {ending}"

    # Tests False
    for string, ending in fixed_tests_False:
        result = solution(string, ending)
        print(f"Testing if '{string}' ends with '{ending}': {result}")
        assert result == False, f"Test failed for: {string}, {ending}"

run_tests()