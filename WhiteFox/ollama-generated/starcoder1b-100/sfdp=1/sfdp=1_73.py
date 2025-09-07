
class Model(torch.nn.Module):
    def __init__(self, d_k=64, d_v=64, dropout_p=0.1, num_heads=8, hidden_dim=256, max_seq_len=50, padding_idx=0):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, d_k, 1)
        self.dropout  = torch.nn.Dropout(p=dropout_p)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        v = torch.matmul(x2, x1)
        k = torch.matmul(x2, self.conv)
        dk  = k * (v / math.sqrt(self.hidden_dim))
        
        scaled_dk = dk.div(torch.exp(dk) + 1e-6)
        scaled_k  = k.div(scaled_dk)

        # Attention over the query and key tensors
        att = torch.matmul(scaled_qk, scaled_dk).softmax(-2)
        new_x  = torch.matmul(att, v) + x1
 
        return self.dropout(new_x)


# Initializing the model
m = Model()
