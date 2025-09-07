
class Model(torch.nn.Module):
    def __init__(self, input_channels=256):
        super().__init__()
        self.linear  = torch.nn.Linear(input_channels * (input_channels + 1) / 2,
                                      3840)

    def forward(self, x):
        v1  =  torch.cat([x] * 9 + [torch.eye(5)], dim=1)
        v2 = v1.view(-1, int((v1.size()[1] * (v1.size()[1] + 1)) / 2),
                     3).transpose(0, 2).contiguous().view(-1,
                                                        self.linear.weight.shape[0])
        v3 = torch.nn.functional.relu(self.linear(v2))
        return v3
# Initializing the model
m = Model()

 # Inputs to the model
__inputs_to_the_model__  = [torch.randn((1, 5), dtype=torch.float) for _ in range(8)]

