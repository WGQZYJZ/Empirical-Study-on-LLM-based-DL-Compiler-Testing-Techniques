v1  = f(x0) # Apply function `f` to input tensor x0
w1  = v1 * (1. - dropout_p) + x0 * dropout_p # Compute the output `o1` by applying dropout, and multiplying it by the scalar `(1-dropout)` plus multiplying it by the scalar `dropout` times the input `x0`
w2  = max_pool2d(w1) # Apply max pooling operation to the output of f(x0). The result will be stored in variable w2
v2  = g(w2)  # Compute the output `o2` by applying function `g` to the input tensor w2. The result will be stored in variable v2


# Initializing the model
m = Model()


# Inputs to the model
x0 = torch.randn(1, 3, 64, 64)

