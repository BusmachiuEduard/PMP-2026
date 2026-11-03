import numpy as np
import scipy.stats as stats
import arviz as az
import matplotlib.pyplot as plt

n_ore = 10
k_total = 180

alpha_0 = 1.0
beta_0 = 0.01


alpha_post = alpha_0 + k_total
beta_post = beta_0 + n_ore


media_post = alpha_post / beta_post
modul_post = max(alpha_post - 1, 0) / beta_post

print(f"Distributia a posteriori: Gamma(alpha={alpha_post}, beta={beta_post})")
print(f"Media a posteriori: {media_post:.4f} apeluri/ora")
print(f"Cea mai probabila valoare (Modul / MAP): {modul_post:.4f} apeluri/ora")


np.random.seed(42)
dist_post = stats.gamma(a=alpha_post, scale=1.0 / beta_post)
posterior_samples = dist_post.rvs(size=20000)

hdi_94 = az.hdi(posterior_samples, prob=0.94)
print(f"Intervalul HDI de 94%: [{hdi_94[0]:.4f}, {hdi_94[1]:.4f}]")

x = np.linspace(dist_post.ppf(0.001), dist_post.ppf(0.999), 500)
y = dist_post.pdf(x)

plt.figure(figsize=(8, 4.5))
plt.plot(x, y, lw=2.5, color="#1f77b4", label="Densitatea a posteriori")

plt.axvline(modul_post, color="darkorange", linestyle="--", lw=2, 
            label=f"Mod (MAP) = {modul_post:.2f}")

x_hdi = np.linspace(hdi_94[0], hdi_94[1], 300)
plt.fill_between(x_hdi, dist_post.pdf(x_hdi), alpha=0.25, color="#1f77b4")
plt.hlines(y=0.005, xmin=hdi_94[0], xmax=hdi_94[1], color="black", lw=4, 
           label=f"94% HDI [{hdi_94[0]:.2f}, {hdi_94[1]:.2f}]")

plt.title("Distributia a posteriori pentru λ (Gamma)")
plt.xlabel("λ (rata medie de apeluri pe ora)")
plt.ylabel("Densitate")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()