
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul  = torch.nn.Linear(64, 32)
    
    def forward(self, q1):
        k1 = torch.randn(q1.shape[0], 64, 64).to(torch.float32)
        
        v1 = torch.rand(k1.shape[0], 32)
        scale_factor  = torch.rand((v1.shape[-2],))
        dropout_p = torch.rand(()).item()
        qk = torch.matmul(q1, k1.transpose(-2, -1))
        scaled_qk = qk * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1) # [B x N x N]
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v1).mean()
        return output


m2 = Model().to('cpu')
out = m2(q1[0].view(-1, 64))
out.shape