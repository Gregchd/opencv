accounts = [[1, 2, 3], [3, 2, 1]]


def maximunW(accounts):
    maxW = 0

    for account in accounts:
        sumW = sum(account)
        maxW = max(maxW, sumW)

    return maxW


maximunW(accounts)
