class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.tensor(256)
 
    def forward(self, query, key, value):
        scaled_qk  = torch.matmul(query, key.transpose(-2, -1)) / (torch.div(self.scale, torch.sqrt(torch.tensor([768]))))
        softmax_qk = torch.nn.functional.softmax(scaled_qk)
 
        return torch.matmul(softmax_qk, value)
