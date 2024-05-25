# Active_Ising_Model
This is an implementation of the Active Ising Model in Python.
##
The Active Ising model is a variant of the traditional Ising model that incorporates activity, making it suitable for studying systems out of equilibrium.

The Hamiltonian of the traditional Ising model is given by:

$$
H = -J \sum_{\langle i,j \rangle} s_i s_j - h \sum_i s_i
$$

where:
- \( H \) is the Hamiltonian.
- \( J \) is the coupling constant.
- \( \langle i,j \rangle \) indicates summation over nearest neighbors.
- \( s_i \) and \( s_j \) are the spins at sites \( i \) and \( j \).
- \( h \) is the external magnetic field.

The Hamiltonian of the Active Ising model is given by:

$$
H = -\sum_{\text{sites } i} \frac{1}{2 \rho_i} \sum_{j=1}^{\rho_i} \sum_{\substack{k \neq j}} S_j^i S_k^i = -\sum_{\text{sites } i} \left[ \frac{m_i^2}{2 \rho_i} - \frac{1}{2} \right]
$$

$$
W(s \rightarrow -s) = \gamma \exp \left( -s \beta \frac{m_i}{\rho_i} \right),
$$

where:
- \( H \) is the Hamiltonian.
- \( \rho_i \) is the local density at site \( i \).
- \( S_j^i \) and \( S_k^i \) are the spins at sites \( j \) and \( k \) within site \( i \).
- \( m_i \) is the local magnetization at site \( i \).
- \( W(s \rightarrow -s) \) is the transition probability of a spin flip.
- \( \gamma \) is a constant.
- \( s \) is the spin variable.
- \( \beta \) is the inverse temperature.
- \( m_i \) is the local magnetization at site \( i \).
- \( \rho_i \) is the local density at site \( i \).

Solon, Alexandre P., and Julien Tailleur. "Flocking with discrete symmetry: The two-dimensional active Ising model." Physical Review E 92.4 (2015): 042119.
