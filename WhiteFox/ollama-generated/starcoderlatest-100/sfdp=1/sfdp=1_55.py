
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_qk = torch.nn.Linear(768, 768)
 
    def forward(self, x1, x2, x3):
        qk = self.linear_qk(torch.cat([x1, x2], dim=-1))
        vq = torch.nn.functional.softmax(qk / scale_factor, dim=0)
        dropout_vq = torch.nn.functional.dropout(vq, p=dropout_p)
        output = dropout_vq.matmul(v_i).transpose(-2, -1).matmul(k_i)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(batch_size, 768, seq_length, device=device)
x2 = torch.randn(batch_size, 768, seq_length, device=device)
x3 = torch.randn(batch_size, 768, seq_length, device=device)
