
class Model(torch.nn.Module):
    def __init__(self, inv_scale=16384):
        super().__init__()
 
        self.inv_scale = torch.tensor([float(inv_scale)])
        self.query = torch.randn(256, 7, 7)
        self.key = torch.randn(256, 7, 7)
 
    def forward(self):
        scaled_dot_product  = torch.matmul(self.query, self.key.transpose(-1, -2)) / \
                              (torch.sqrt(torch.tensor([float(int(8 * self.inv_scale))])))
 
        attention_weights  = scaled_dot_product.softmax(dim=-2)
        output  = torch.matmul(attention_weights, torch.randn(7, 7)).relu()
        return output
 
# Initializing the model and setting random seeds for query/key tensors.
seed1  = np.random.randint(0, int(1e6)) + 9538
seed2  = np.random.randint(int(1e7), int(2e7)) + 47
 
query = torch.randn(int(1e6) * seed1).reshape(-1, 1, 1).float() / \
    (torch.tensor([np.sqrt(seed1)])) - query_bias
key   = torch.randn(256 * int(8), seed1 + seed2).reshape(-1, 7, 7)
 
model = Model().cuda()
query = query.cuda(); key = key.cuda()
 
 
# Inputs to the model and setting random seeds for query/key tensors.
query_bias  = torch.randn(3804952 + seed1) * (seed1 % int(1e6)) / \
              (torch.tensor([np.sqrt(int(1e6))]))
seed2      = np.random.randint(int(1e7), int(2e7)) + 4308
 
# Set the seeds in numpy, pytorch and cuda for deterministic random number generators.
np.random.seed(seed1); torch.manual_seed(seed1)
 
query = query.cuda(); key = key.cuda()
 
 
