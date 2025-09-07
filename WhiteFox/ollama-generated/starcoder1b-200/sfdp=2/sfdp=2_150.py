
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(d_model, d_model)  # Embedding Layer
        self.linear2 = torch.nn.Linear(d_model, d_model)  # Embedding Layer

    def forward(self, x):
        batch_size = x.shape[0]  # Batch size of the input

        # Compute hidden state for all time steps in batch
        h_n = self.linear1(x)
        c_n = torch.zeros((batch_size, d_model))
        h_n_t = [h_n]

        # Compute context vector for each time step and concatenate them to a 2D array
        for t in range(tmax):
            h_t = self.linear1(x[:, (t+1):])
            c_t = torch.cat([c_n, self.linear2(h_t)], dim=-1)

            # Set the hidden state of time step t to the new context vector
            h_n_t.append(h_n)
            c_n = c_t

        # Compute the output of LSTM with new context vectors
        output, (hidden_n, cell_n) = self.rnn(h_n_t, c_n)  # Output from LSTM, hidden state and cell state
        return output


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, d_model)
output = m(input_tensor)
