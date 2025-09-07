
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = input_tensor.permute(0, 2, 1)
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 2)

# Correctly identified patterns in the sample model
__output__  = m(x1)

## Sample Input to be validated:
t0_input = torch.rand(256)

 ## Patterns found in this example (inferred from the previous 2 lines)
## t0: The 3rd line is 't1 = t0.permute(0, 1)', which contains a permute operation with one argument 't0'
## t1: The 4th line is 't2 = torch.nn.functional.linear(t1)
## The pattern cannot be used in the validation.

# Validation - Correctness of Patterns found by analysis

__Pattern__  : t0.permute(0, 1)

__Correctness check__ : Yes. We detected pattern 't0' and then identified the pattern 't1' as a result which contains a permute operation with one argument 't0'. Hence we can conclude that the pattern 't0' is correctly used in the 't1'

 __Pattern__  : t2 = torch.nn.functional.linear(t1)

__Correctness check__: No, We detected 3 patterns ('t0', 't1') and we have only 2 identified. The pattern 't2' is not present in the pattern list while 't0' and 't1' are. Hence it means that these 3 patterns cannot be used to generate the new PyTorch model
