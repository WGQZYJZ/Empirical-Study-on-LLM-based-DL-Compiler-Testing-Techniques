
class Model(torch.nn.Module):
    def __init__(self, out=2048):
        super().__init__()

        self.embedding = torch.nn.EmbeddingBag(317956, 784)
        self.fc1   = nn.Linear(in_features=784*out,
                              out_features=10 * out)

    def forward(self, x):
        
        v1  = self.embedding(x, [None for _ in range(len(x))], scale=True).reshape(-1, len(x), 392)
        v2  = torch.tanh(v1[:, :, :784].mean(axis=-2))
        v3  = F.dropout(torch.cat((v2, v1[:, :, 784:]), axis=0))

        return self.fc1(v3).reshape(-1, len(x), 10 * out)


# Initializing the model
m  = Model()


# Inputs to the model
x = torch.randint(low=29658, high=47108, size=(int(np.random.uniform()*3+3),))
