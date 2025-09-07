class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.randn(1, 64)
        self.key  = torch.randn(3200, 768)

    @staticmethod
    def compute_scale(dim, dropout):
        return dim / (dropout * math.sqrt(math.prod(dim)))
 
    def forward(self, x1):

        scale_factor = self.compute_scale([len(x1)], p=0.25).item()
        qk  = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk  = qk.mul(scale_factor)
        softmax_qk  = scaled_qk.softmax(dim=-1)  
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.25)  
        output  = dropout_qk.matmul(value)
        return output
