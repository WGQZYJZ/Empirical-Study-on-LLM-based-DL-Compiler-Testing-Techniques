
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(d_model, d_vocab)

    def forward(self, x):
        # TODO: Implement this function
