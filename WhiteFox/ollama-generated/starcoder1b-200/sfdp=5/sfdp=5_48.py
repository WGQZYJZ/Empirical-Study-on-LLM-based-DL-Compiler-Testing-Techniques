
class Model(torch.nn.Module):
    def __init__(self, vocab_size=256):
        super().__init__()
        self.vocab_size = vocab_size
 
    def forward(self, x1, x2):
        batch_size = x1.size(0)
        dim  = x1.size(-1)
 
        