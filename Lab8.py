#Cole McLean CSCI 161
def madhava_leibniz(n):
    return ((-1) ** n) / (2 * n + 1)


def calculate_pi(num_terms):
    pi_approximation = 0
    for i in range(num_terms):
        pi_approximation += madhava_leibniz(i)
    return pi_approximation * 4


num_terms = 1000
approx_pi = calculate_pi(num_terms)
print("Approximation of π using {} terms: {}".format(num_terms, approx_pi))
