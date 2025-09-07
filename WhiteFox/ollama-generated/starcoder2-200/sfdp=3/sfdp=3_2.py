
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.tensor(0.5)
        self.dropout_p  = 0.3
        self.query  = torch.randn(1, 2048, 7, 7).float()
        self.key  = torch.randn(1, 2048, 7, 7).float()
        self.value  = torch.randn(1, 512, 7, 7).float()
 
    def forward(self):
        qk  = torch.matmul(self.query, self.key.transpose(-2, -1))
        scaled_qk  = qk * self.scale
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output  = dropout_qk.matmul(self.value)
        return output

# Initializing the model