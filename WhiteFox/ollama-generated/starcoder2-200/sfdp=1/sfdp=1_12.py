class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(2048, 1536)
        self.key = torch.randn(768, 1536)
        self.value = torch.randn(2048, 768)
 
    def forward(self):
        inv_scale_factor = (torch.rand(()) * .9 + .1).item() # randomly initialize the scale factor between .1 and .9
        dropout_p = torch.rand(()).item()
 
        qk = torch.matmul(self.query, self.key.transpose(-2,-1))
        scaled_qk  = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(self.value)
        return output
