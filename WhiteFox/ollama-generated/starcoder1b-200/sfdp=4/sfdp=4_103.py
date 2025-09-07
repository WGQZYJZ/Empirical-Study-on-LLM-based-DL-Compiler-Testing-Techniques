
class Model(torch.nn.Module):
    def __init__(self, vocab_size: int):
        super().__init__()
        self.vocab_size = vocab_size
 
    def forward(self, x1, x2):
        