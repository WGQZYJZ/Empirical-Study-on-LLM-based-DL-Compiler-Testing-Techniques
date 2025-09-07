
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2)  # Matrix multiplication on two tensors of shape (280, 543), and (543, 73). 
        return v1 + self.__input_arg_1

# Initializing the model