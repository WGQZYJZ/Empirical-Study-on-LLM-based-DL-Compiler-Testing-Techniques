
class Attention(torch.nn.Module):
    def __init__(self, hidden_dim):
        super().__init__()
        self.w = torch.nn.Parameter(torch.randn(1, 1, hidden_dim))
 
    def forward(self, qk: torch.Tensor):
        softmax_qk = softmax(qk) # TODO: Replace this placeholder with your implementation
        