# -1 - What is a CRUD? What is a REST?

# 0. - What is a JSON? What is a XML? What is their structure?

# 1. What data types are you familiar with in Python? Do you know any specific function for a specific data type?

# 2. What's the difference between them?

# 3. How to import HIDDEN_VARIABLE from the test_data module located in the same directory as the current file?

# 4. How do you find out what type the variable is?

# 5. How do you define a function?

# 6. How do you define a class?

# 7. Difference between method/function, constant/variable?

# 8. What is the "self" that is used as an argument in a class method? How to write the "constructor" of a class?

# 9. How do you draw the pattern below using a print("*")?
# *
# * *
# * * *
# * * * *
# * * * * *

# 10. Print the maximum and lowest numbers from the list.
numbers: list[int] = [1, 10, 22, 11, 42, 0, 32, 41]

# 11. Print customer names from dict_values, but leave out the excustomers.
dict_values: dict[str, str] = {
    "customer1": "Jan Novak",
    "customer2": "Petr Novak",
    "customer3": "Jirka Novak",
    "customer4": "Ondra Novak",
    "excustomer1": "Tomas Novotny",
    "excustomer2": "Jirka Novotny",
    "excustomer3": "Ondra Novotny",
    "excustomer4": "Petr Novotny",
}

# 12. If you have not already done so, write it as a list comprehension.


# 13. What is wrong with those classes? Can you fix them?
#You can delete or move the code anywhere, but only the assert_lie method can be modified.

class TruthTeller:
    def __init__(self, truth: bool) -> None:
        self.truth = truth

    def assert_truth(self) -> bool:
        return True


class TruthMixin:
    def assert_truth(self) -> bool:
        return super().assert_truth() and self.truth is True



class IsYourThruthReallyTruth(TruthTeller, TruthMixin):
    def assert_truth(self) -> bool:
        """
        Returns True if self.truth is actually a boolean True
        """
        return False


class IsYourTruthLie(IsYourThruthReallyTruth):
    def assert_lie(self) -> bool:
        """
        Returns True if self.truth is not a boolean True.
        """
        return False


#print(IsYourThruthReallyTruth(True).assert_true(), "should be True")
# Do you know why this should be a False?
#print(IsYourThruthReallyTruth(1).assert_true(), "should be False")
#print(IsYourThruthReallyTruth("true").assert_true(), "should be False")
#print(IsYourTruthLie(True).assert_lie(), "should be False")
#print(IsYourTruthLie(0).assert_lie(), "should be True")
#print(IsYourTruthLie(1).assert_lie(), "should be True")
#print(IsYourTruthLie(False).assert_lie(), "should be True")


# 14. What is wrong with this function?
def append_to_list(value: int, values_list: list[int] = []) -> list[int]:
    values_list.append(value)
    return values_list

# what will be printed?
#print(append_to_list(10))
# what will be printed?
#print(append_to_list(20))
