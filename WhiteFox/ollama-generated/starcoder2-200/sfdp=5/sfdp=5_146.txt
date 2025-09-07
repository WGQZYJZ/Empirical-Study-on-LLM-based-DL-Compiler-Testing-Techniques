
class Model(torch.nn.Module):
    def __init__(self, d_model: int = 768) -> None:
        super().__init__()

        self.d_model = d_model

        self.qk = torch.nn.Linear(in_features=320 * d_model + 320 * d_model // 4, out_features=d_model, bias=False)

    def forward(self, input):
        self.qk(input)


model = Model()

inputs = torch.randn(1, 3, 64, 64)
inputs = inputs / inputs[0] * 255; # Make the image between -1 and 1

inputs = torch.randperm(inputs).view(-1, inputs.size()[-3], inputs.size()[-2], inputs.size()[-1])
