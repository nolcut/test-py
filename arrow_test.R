arrow_test <- function() {
  b <- faasr_arrow_s3_bucket()
  cat("Arrow S3 bucket:", format(b), "\n")

  invocationid <- faasr_invocation_id()
  cat("InvocationID:", format(invocationid), "\n")
}