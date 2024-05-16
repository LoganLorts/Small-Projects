def find_total(cookies, location, num_friend):
    total = 0
    cookies = cookies.copy()
    #base
    if cookies[location] == 0:
        return 0
    
    #recursive
    if location == 0:
        if cookies[location] >= num_friend:
            cookies[location] -= num_friend
            total += num_friend
        else:
            total += cookies[location]
            num_friend = cookies[location]
            cookies[location] = 0
        next_location = cookies.index(max(cookies[1], cookies[2]))
        total += find_total(cookies, next_location, num_friend)
    elif location == 1:
        if cookies[location] >= num_friend:
            cookies[location] -= num_friend
            total += num_friend
        else:
            total += cookies[location]
            num_friend = cookies[location]
            cookies[location] = 0
        next_location = cookies.index(max(cookies[0], cookies[2]))
        total += find_total(cookies, next_location, num_friend)
    elif location == 2:
        if cookies[location] >= num_friend:
            cookies[location] -= num_friend
            total += num_friend
        else:
            total += cookies[location]
            num_friend = cookies[location]
            cookies[location] = 0
        next_location = cookies.index(max(cookies[1], cookies[0]))
        total += find_total(cookies, next_location, num_friend)
    #print(cookies, total)
    return total


# Main
if __name__ == "__main__":
    user_input = input().split()
    num_friend = int(user_input[0])
    cookies = []
    for i in user_input[1:]:
        cookies.append(int(i))
    start = cookies.index(max(cookies))
    #print(start, cookies)
    print(find_total(cookies, start, num_friend))