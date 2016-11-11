# Generates 100 nodes with x and y spatial coordinates
    set.seed(5)
    x = rnorm(100) * 100
    y = rnorm(100) * 100
    data = data.frame(x, y)
    
#We need a distance matrix that helps us generate an adjacency matrix in future steps.

    dist <- as.matrix(dist(data))

#We can write a function in R, which generates adjacency matrices based on the threshold distance _d_. 

    nt <- function(d) {
        DM <- dist[] < d
        diag(DM) = 0
        return(DM)
    }
