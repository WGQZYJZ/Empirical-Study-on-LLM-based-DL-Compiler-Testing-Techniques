
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(d_model, d_k)
        self.key = torch.nn.Linear(d_model, d_k)
        self.value = torch.nn.Linear(d_model, d_v)
        self.dropout = torch.nn.Dropout(p=dropout_p)
 
    def forward(self, x1, x2):
        q  = self.query(x1)
        k  = self.key(x2)
        v  = self.value(x2)
        # Apply mask to the input masks
        m1 = x1.unsqueeze(-1).expand_as(q).bool()
        m2 = x2.unsqueeze(-1).expand_as(k).bool()
        mask = m1 & m2
        k = k * (~mask.float()).transpose(-2, -1)  # Set key to zero for the masked positions in x1
        v = v * (~mask.float()).transpose(-2, -1)  # Set value to zero for the masked positions in x2
        # Calculate scaled dot product of the query and key tensors
        qk = torch.matmul(q, k).div(self.scale_factor ** (-0.5))
        # Apply softmax on the scaled dot product output (qk)
        qk_softmax  = qk.softmax(-1)
        # Calculate dropout output for the scaled dot product and the value tensors
        dropout_qk = torch.nn.functional.dropout(qk_softmax, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output


# Initializing the model
m = Model()


