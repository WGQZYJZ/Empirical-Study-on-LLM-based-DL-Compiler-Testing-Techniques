
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc   = torch.nn.Linear(4096, 10)
 
    def forward(self, x1, x2):
        query = torch.cat((x1, x2), dim=-1)
        key   = torch.cat((x1, x2), dim=-1)
        # Scale the query and the key tensors by a factor
        scale_factor  = torch.nn.functional.softplus(self.fc(query))
        scaled_query  = query.mul(scale_factor)
        scaled_key    = key.mul(scale_factor)
        softmax_qk     = F.softmax(scaled_query, dim=-1)
        dropout_qk     = F.dropout(softmax_qk, p=dropout_p)
        output         = dropout_qk.matmul(scaled_key)
        return F.log_softmax(self.fc(output), dim=-1)


# Initializing the model
m  = Model()


