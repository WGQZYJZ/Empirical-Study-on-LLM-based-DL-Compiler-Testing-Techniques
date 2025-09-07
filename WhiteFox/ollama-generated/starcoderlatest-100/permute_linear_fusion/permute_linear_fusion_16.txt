
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 2) # [torch.Size([1, 3, 2]), torch.Size([1, 3, 2])]
__output_1 = m(x1[0])
__output_2 = m(x1[1])


# Please generate a valid PyTorch model example with public PyTorch APIs meets the specified requirements. Plus, please also generate the input tensor for the newly generated model. The model should be different from the previous one.


