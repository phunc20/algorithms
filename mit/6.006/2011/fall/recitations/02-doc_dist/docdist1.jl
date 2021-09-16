

function inner_product(a1, a2)
  somme = 0
  for (word1, count1) in a1
    for (word2, count2) in a2
      if word2 == word1
        somme += count1 * count2
        break
      end
    end
  end
  return somme
end

function len(a)
  return √(innter_product(a, a))
end

function θ(a1, a2)
  cosθ = inner_product(a1, a2) / √(inner_product(a1, a1) * inner_product(a2, a2))
  return acos(cosθ)
end


