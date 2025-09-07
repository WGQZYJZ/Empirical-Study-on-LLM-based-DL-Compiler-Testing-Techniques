
class Model(torch.nn.Module):
    def __init__(self, ):
        super().__init__()
        self.conv  = torch.nn.Conv2d(16, 33, 3)

    def forward(self, input):
        output =  conv(input_tensor, torch.nn.Functional.batch_norm(self.conv))

m  = Model()
