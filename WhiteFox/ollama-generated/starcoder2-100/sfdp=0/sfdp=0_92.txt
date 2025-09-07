
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale = 1200):
        super().__init__()
        self.softmax  = torch.nn.Softmax(-1)
 
    def forward(self, qkvw):
        scaled_dot_product  = torch.matmul(qkvw[0], qkvw[1].transpose(-2, -1)) / qkvw[-1] 
        attention_weights   = self.softmax(scaled_dot_product).unsqueeze(-1)
        output              = attention_weights.matmul(qkvw[2]).squeeze()
        return [output]
