
class Model(torch.nn.Module):
    def __init__(self, a: int) -> None:
        super().__init__()

    def forward(self, input1: torch.Tensor, input2: torch.Tensor = 3) -> tuple[int]:
        permuteA  = input_tensor_A.permute(...) # Permute the input tensor A
        permuteB  = input_tensor_B.permute(...) # Permute the input tensor B

        out = permuteA.bmm(permuteB) or permuteA @ permuteB
        
        return [out]


# Initializing the model with a constant argument for 'a' parameter, and no argument for 'b', then call it.

a_param  = torch.nn.Parameter(torch.zeros((2)))
model  = Model(3) # Initialize the model. In this case, 'a' is fixed at 0 with a value that can be ignored by observers. 
result1, result2  = model(input_tensor_A, input_tensor_B)

