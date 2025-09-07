class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv1d(256, 3072)
        output  = torch.nn.functional.batch_norm(conv(x1)) 
        return output
