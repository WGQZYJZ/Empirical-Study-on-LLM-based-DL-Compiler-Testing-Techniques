
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    @torch.jit._function()
    def forward(input_tensor):
        conv = input_tensor.permute(0, 2, 1)
        bn = torch.nn.functional.batch_norm(...)
        return bn(conv(input_tensor))


# Inputs to the model
x1 = torch.randn(1, 2, 2)
