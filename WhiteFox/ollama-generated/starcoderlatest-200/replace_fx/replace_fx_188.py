 1 (dropout)
class Model1(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.rand_like(x1, dtype=torch.float32) # Generate a tensor with the same size as input_tensor filled with random numbers
        t2 = torch.nn.functional.dropout(x1, p=0.5, inplace=False) # Apply dropout to the input tensor (p: probability; inplace: whether to use inplace mode.)
        return t2 + x1
# Model 2 (randomness-based replacement)
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        with gm.GraphMode():
            gm.enable_op("lowmem_dropout")
            t1 = torch.rand_like(x1, dtype=torch.float32) # Generate a tensor with the same size as input_tensor filled with random numbers
            t2 = gm.lowmem_dropout(x1, p=0.5)  # Apply dropout to the input tensor (p: probability; inplace: whether to use inplace mode.)
        return t2 + x1


# Inputs to the model
x1 = torch.randn(1, 4, 6)
