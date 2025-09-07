
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc_q = torch.nn.Linear(768, 512)
        self.fc_k = torch.nn.Linear(768, 512)
 
    def forward(self, x):
        k = self.fc_k(x)
        q = self.fc_q(x)
        scaled_qk = torch.matmul(q, k.transpose(-2, -1)) * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, v)
        return output


# Inputs to the model
x = torch.randn(batch_size, 768, sequence_length)
