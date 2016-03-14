
class qr_pogs():

    def __init__(self):

        self.qr_pogs_def = """
            qr_pogs <- function(X, y, tau, params = list(), dual = TRUE){
              n <- nrow(X)
              p <- ncol(X)
              if(dual){
                f <- list(h = kIndEq0(p), b = (1 - tau) * apply(X,2,sum))
                g <- list(h = kIndBox01(n), d = -y)
                z <- pogs(t(X), f, g, params = params)$v
              }
              else{
                f <- list(h = kAbs(n), b = y, c = 0.5, d = (0.5 - tau))
                g <- list(h = kZero(p))
                z <- pogs(X, f, g, params = params)$x
              }
              c(z)
            }
        """
        pass