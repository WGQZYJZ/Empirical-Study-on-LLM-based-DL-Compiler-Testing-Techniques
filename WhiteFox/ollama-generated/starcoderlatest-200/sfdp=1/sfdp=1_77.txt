
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(d_model, d_key)
 
    def forward(self, q, k, v):
        att1 = self.attn(q).transpose(-2, -1) # Compute the attention map of each query tensor to all key tensors
        att2 = self.attn(k).transpose(-2, -1) # Compute the attention map of all key tensors to all value tensors
        scaled_att  = att1 / scale_factor * att2 # Scale the attention maps by a scale factor
        dropout_scaled_att = torch.nn.functional.dropout(scaled_att, p=dropout_p) # Apply dropout with probability 0.1
        return dropout_scaled_att
