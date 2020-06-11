def least_cost(costs):
    row = len(costs)
    col = len(costs[0])
    # print(row,col)
    i = row - 1
    j = 0
    least_cost_value = costs[-1][0]
    count = 0
    while True:
        print(i, j) 
        if i == 0 and j == col-1:
            break
        else:
            if j == col-1:
                least_cost_value += costs[i-1][j]
                i = i-1
            elif i == 0:
                least_cost_value += costs[i][j+1]
                j = j+1
            else:
                if least_cost_value + costs[i-1][j] < least_cost_value + costs[i][j+1]:
                    least_cost_value += costs[i-1][j]
                    i = i-1
                    count+=1
                else:
                    least_cost_value += costs[i][j+1]
                    j = j+1
                    count+=1

    return least_cost_value


def least_cost_2(costs, i,j):
    col = len(costs[0])
    # print(row,col)
    least_cost_value = costs[i][j]
    count = 0
    while True:
        print(i, j) 
        if i == 0 and j == col-1:
            break
        else:
            if j == col-1:
                least_cost_value += costs[i-1][j]
                i = i-1
            elif i == 0:
                least_cost_value += costs[i][j+1]
                j = j+1
            else:
                if least_cost_value + costs[i-1][j] < least_cost_value + costs[i][j+1]:
                    least_cost_value += costs[i-1][j]
                    i = i-1
                    count+=1
                else:
                    least_cost_value += costs[i][j+1]
                    j = j+1
                    count+=1

    return least_cost_value

def least_cost_3(costs):
    row = len(costs)
    col = len(costs[0])
    # print(row,col)
    i = row - 1
    j = 0
    least_cost_value = costs[-1][0]
    path_coordinates = []
    while True:
        print(i, j) 
        if i == 0 and j == col-1:
            break
        else:
            if j == col-1:
                least_cost_value += costs[i-1][j]
                i = i-1
                path_coordinates.append((i,j))
            elif i == 0:
                least_cost_value += costs[i][j+1]
                j = j+1
                path_coordinates.append((i,j))
            else:
                if least_cost_value + costs[i-1][j] < least_cost_value + costs[i][j+1]:
                    least_cost_value += costs[i-1][j]
                    i = i-1
                    path_coordinates.append((i,j))
                else:
                    least_cost_value += costs[i][j+1]
                    j = j+1
                    path_coordinates.append((i,j))

    return least_cost_value, path_coordinates