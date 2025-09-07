
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(1024, 512)
        self.linear_k = torch.nn.Linear(1024, 512)
        self.linear_v = torch.nn.Linear(1024, 512)
 
    def forward(self, query):
        q = self.linear_q(query).unsqueeze(-1).unsqueeze(-1) # add a dimension to the inputs so that it can be multiplied by k
        k = self.linear_k(query).unsqueeze(1).unsqueeze(1) # add another dimension and repeat one of its dimensions 3 times in each axis
        v = self.linear_v(query).unsqueeze(2).unsqueeze(2)
        qk = torch.matmul(q, k)
        scaled_qk = qk / inv_scale_factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        output = torch.matmul(softmax_qk, v)
        return output


# Inputs to the model
query  = torch.randn(1024, num_keys, dtype=torch.float32)
