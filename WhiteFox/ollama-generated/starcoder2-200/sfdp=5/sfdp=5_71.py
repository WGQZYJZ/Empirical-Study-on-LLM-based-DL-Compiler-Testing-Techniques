
class Model(torch.nn.Module):
    def __init__(self, embedder1):
        super().__init__()

        self.embedder1 = embedder1
        self.layer1  = torch.nn.Linear(512, 32)
        self.layer2  = torch.nn.Linear(768, 9)

    def forward(self, x):
        v4_0 = self.layer1(x).tanh()
        v5 = torch.softmax(v4_0, dim=-1)
        return [v3] + [self.embedder2(v1)]

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(768)

 