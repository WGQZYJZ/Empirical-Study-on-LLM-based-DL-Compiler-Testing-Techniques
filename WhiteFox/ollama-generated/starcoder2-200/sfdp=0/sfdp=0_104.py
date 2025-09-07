class MSA(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 1 / torch.sqrt(torch.tensor([2048]))
    
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / self.scale
        attention_weights = scaled_dot_product.softmax(dim=-1) # Softmax along the last dimension of the tensor
        output  = attention_weights.matmul(value)
        
        return output
