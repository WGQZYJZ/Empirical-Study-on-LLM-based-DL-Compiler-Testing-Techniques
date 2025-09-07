
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.25)  # Dropout layer is invoked
        return v1


# Initializing the model
m = Model()
gm = torch_analyzer.compile(m, (torch.randn(3, 4, 3),))
gm = gm.eval()
gm.backward((torch.randn(1, 2, 2)), retain_graph=True)

