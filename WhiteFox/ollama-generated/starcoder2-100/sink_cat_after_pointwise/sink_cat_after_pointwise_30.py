
class Model(torch.nn.Module):
    def __init__(self, num_classes=1000):
        super().__init__()
        self._model = torch.hub.load('pytorch/vision:v0.9.0', 'resnet50', pretrained=True)

    def forward(self, x):
        v  = self._model(x).view(-1, 32 * 47 * 47)
        return torch.nn.functional.linear(v, 8*8*512)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.rand(1, 3, 224, 224)
__output__  = m(x)

