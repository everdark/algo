# given a 3-dimensional array, or a stack of matrices
# this algorithm sorts each element along the third dimension via insertion sort

# notice that this is by far slower than simply do: 
# aperm(apply(object, 1:2, sort), c(2,3,1))


insertion_sort <- function(object) {
    for (col in 1:ncol(object)) {
        for (row in 1:nrow(object)) {
            for (j in 2:dim(object)[3]) {
                key <- object[row,col,j]
                i <- j - 1
                while (key < object[row,col,i]) {
                    swap <- object[row,col,i+1]
                    object[row,col,i+1] <- object[row,col,i]
                    object[row,col,i] <- swap
                    i <- i - 1
                    if (i == 0) break
                }
            }
        }
    }
    object
}

object <- array(rnorm(9), dim=c(3,2,5))
object

insertion_sort(object)