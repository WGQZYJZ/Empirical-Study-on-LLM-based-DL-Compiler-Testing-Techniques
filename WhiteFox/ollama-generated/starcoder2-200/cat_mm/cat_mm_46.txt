
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1: torch.Tensor,  # pylint: disable=arguments-differ
                input2: List[torch.Tensor]):
        t1 = torch.mm(input1, input2)  # Matrix multiplication of two tensors
        t2 = torch.cat([t1] * len(input2))
        return t2


# Initializing the model
m = Model()


# Inputs to the model (first input is a torch tensor and second one is a list containing the torch tensors)
x1 = torch.randn(3, 4)
x2 = [torch.randn(50, 8), torch.randn(60, 9)]
