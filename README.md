import React from 'react';
import { Code2, Zap, Wrench, Trophy, Star, AlertTriangle, CheckCircle, Brain, Target, BookOpen, Lightbulb, Shield, Users, GitBranch, Rocket, Bug, RefreshCw, FileText } from 'lucide-react';

const README = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900 text-white">
      {/* Header */}
      <div className="relative overflow-hidden bg-gradient-to-r from-blue-600 via-purple-600 to-teal-600 py-20 px-6">
        <div className="absolute inset-0 bg-black/20"></div>
        <div className="relative max-w-6xl mx-auto text-center">
          <div className="inline-flex items-center gap-3 mb-6">
            <Brain className="w-12 h-12 text-white" />
            <h1 className="text-5xl font-bold bg-gradient-to-r from-white to-blue-200 bg-clip-text text-transparent">
              IA Générative pour le Développement
            </h1>
          </div>
          
          <div className="flex justify-center gap-4 mb-8 flex-wrap">
            <span className="px-4 py-2 bg-blue-500/20 backdrop-blur-sm rounded-full border border-blue-400/30 text-blue-200 font-medium">
              AI Development
            </span>
            <span className="px-4 py-2 bg-yellow-500/20 backdrop-blur-sm rounded-full border border-yellow-400/30 text-yellow-200 font-medium">
              Python
            </span>
            <span className="px-4 py-2 bg-green-500/20 backdrop-blur-sm rounded-full border border-green-400/30 text-green-200 font-medium">
              Status: Complete
            </span>
          </div>
        </div>
        
        {/* Animated background elements */}
        <div className="absolute top-10 left-10 w-20 h-20 bg-blue-400/10 rounded-full blur-xl animate-pulse"></div>
        <div className="absolute bottom-10 right-10 w-32 h-32 bg-purple-400/10 rounded-full blur-xl animate-pulse delay-700"></div>
      </div>

      <div className="max-w-6xl mx-auto px-6 py-12">
        {/* Table of Contents */}
        <div className="mb-16">
          <h2 className="text-3xl font-bold mb-8 flex items-center gap-3">
            <BookOpen className="w-8 h-8 text-blue-400" />
            Table des Matières
          </h2>
          <div className="grid md:grid-cols-3 gap-4">
            {[
              { icon: Target, title: "Partie 1 : Choix de la Solution", color: "from-blue-500 to-cyan-500" },
              { icon: Zap, title: "Partie 2 : Génération de Code", color: "from-purple-500 to-pink-500" },
              { icon: Wrench, title: "Partie 3 : Débogage et Amélioration", color: "from-green-500 to-teal-500" }
            ].map((item, index) => (
              <div key={index} className="group cursor-pointer">
                <div className="p-6 bg-slate-800/50 backdrop-blur-sm rounded-xl border border-slate-700/50 hover:border-slate-600/50 transition-all duration-300 hover:scale-105">
                  <div className={`w-12 h-12 rounded-lg bg-gradient-to-r ${item.color} flex items-center justify-center mb-4 group-hover:scale-110 transition-transform`}>
                    <item.icon className="w-6 h-6 text-white" />
                  </div>
                  <h3 className="font-semibold text-lg text-white group-hover:text-blue-300 transition-colors">
                    {item.title}
                  </h3>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Partie 1 */}
        <section className="mb-16">
          <div className="flex items-center gap-4 mb-8">
            <div className="w-16 h-16 rounded-full bg-gradient-to-r from-blue-500 to-cyan-500 flex items-center justify-center">
              <Target className="w-8 h-8 text-white" />
            </div>
            <h2 className="text-4xl font-bold">Partie 1 : Choix de la Solution</h2>
          </div>

          {/* Solution Retenue */}
          <div className="mb-12">
            <div className="text-center mb-8">
              <Trophy className="w-16 h-16 text-yellow-400 mx-auto mb-4" />
              <h3 className="text-2xl font-bold mb-4">Solution Retenue</h3>
              <div className="inline-block px-8 py-4 bg-gradient-to-r from-green-500 to-teal-500 rounded-full text-xl font-bold">
                ChatGPT (OpenAI)
              </div>
            </div>
            <p className="text-lg text-slate-300 text-center max-w-4xl mx-auto leading-relaxed">
              Modèle d'intelligence artificielle développé par OpenAI, capable de comprendre et de générer du langage naturel. 
              Utilisé comme assistant de codage pour générer, corriger, expliquer ou améliorer du code dans plusieurs langages de programmation.
            </p>
          </div>

          {/* Avantages & Limites */}
          <div className="grid lg:grid-cols-2 gap-8 mb-12">
            {/* Avantages */}
            <div className="bg-gradient-to-br from-green-900/30 to-emerald-900/30 backdrop-blur-sm rounded-2xl border border-green-500/20 p-8">
              <div className="flex items-center gap-3 mb-6">
                <CheckCircle className="w-8 h-8 text-green-400" />
                <h3 className="text-2xl font-bold text-green-300">Avantages</h3>
              </div>
              <div className="space-y-4">
                {[
                  { icon: "💬", title: "Multifonctionnel", desc: "Peut expliquer du code, le commenter, le corriger ou générer de nouvelles fonctionnalités à partir d'une simple description" },
                  { icon: "🌍", title: "Polyglotte", desc: "Prend en charge une large variété de langages de programmation (Python, JavaScript, C, HTML, etc.)" },
                  { icon: "⏱️", title: "Gain de productivité", desc: "Permet d'accélérer le prototypage, la recherche d'erreurs ou l'exploration de solutions alternatives" }
                ].map((item, index) => (
                  <div key={index} className="flex gap-4 p-4 bg-green-500/10 rounded-lg border border-green-500/20">
                    <span className="text-2xl">{item.icon}</span>
                    <div>
                      <h4 className="font-semibold text-green-200 mb-1">{item.title}</h4>
                      <p className="text-slate-300 text-sm">{item.desc}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Limites */}
            <div className="bg-gradient-to-br from-red-900/30 to-orange-900/30 backdrop-blur-sm rounded-2xl border border-red-500/20 p-8">
              <div className="flex items-center gap-3 mb-6">
                <AlertTriangle className="w-8 h-8 text-red-400" />
                <h3 className="text-2xl font-bold text-red-300">Limites et Inconvénients</h3>
              </div>
              <div className="space-y-4">
                {[
                  { icon: "❌", title: "Précision variable", desc: "Peut générer du code incorrect ou inefficace, nécessitant une vérification attentive" },
                  { icon: "📎", title: "Risque de dépendance", desc: "Peut limiter l'apprentissage actif chez certains étudiants ou développeurs débutants" },
                  { icon: "🔒", title: "Accès limité", desc: "Pas d'accès direct au projet ou aux fichiers, contrairement à certains IDE intégrés" }
                ].map((item, index) => (
                  <div key={index} className="flex gap-4 p-4 bg-red-500/10 rounded-lg border border-red-500/20">
                    <span className="text-2xl">{item.icon}</span>
                    <div>
                      <h4 className="font-semibold text-red-200 mb-1">{item.title}</h4>
                      <p className="text-slate-300 text-sm">{item.desc}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Cas d'Usage */}
          <div className="bg-slate-800/50 backdrop-blur-sm rounded-2xl border border-slate-700/50 p-8">
            <h3 className="text-2xl font-bold mb-6 flex items-center gap-3">
              <Rocket className="w-7 h-7 text-blue-400" />
              Cas d'Usage Typiques
            </h3>
            <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
              {[
                { icon: "🚀", title: "Génération rapide", desc: "de fonctions ou d'algorithmes à partir d'une description en langage naturel" },
                { icon: "🧪", title: "Débogage", desc: "ou explication de code complexe" },
                { icon: "📖", title: "Apprentissage", desc: "de nouveaux langages ou frameworks" },
                { icon: "📝", title: "Documentation", desc: "génération de commentaires ou tests unitaires" }
              ].map((item, index) => (
                <div key={index} className="p-4 bg-slate-700/50 rounded-lg border border-slate-600/50 hover:bg-slate-700/70 transition-colors">
                  <div className="text-3xl mb-2">{item.icon}</div>
                  <h4 className="font-semibold text-blue-300 mb-1">{item.title}</h4>
                  <p className="text-slate-400 text-sm">{item.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Partie 2 */}
        <section className="mb-16">
          <div className="flex items-center gap-4 mb-8">
            <div className="w-16 h-16 rounded-full bg-gradient-to-r from-purple-500 to-pink-500 flex items-center justify-center">
              <Zap className="w-8 h-8 text-white" />
            </div>
            <h2 className="text-4xl font-bold">Partie 2 : Génération de Code</h2>
          </div>

          {/* Analyse Comparative */}
          <div className="bg-slate-800/50 backdrop-blur-sm rounded-2xl border border-slate-700/50 p-8 mb-12">
            <h3 className="text-2xl font-bold mb-6 flex items-center gap-3">
              <Code2 className="w-7 h-7 text-purple-400" />
              Exercice 2.1 : Analyse Comparative
            </h3>
            
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b border-slate-600">
                    <th className="text-left p-3 font-semibold text-purple-300">Aspect</th>
                    <th className="text-center p-3 font-semibold text-blue-300">Code 1</th>
                    <th className="text-center p-3 font-semibold text-green-300">Code 2</th>
                    <th className="text-center p-3 font-semibold text-yellow-300">Code 3</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-700">
                  {[
                    { aspect: "🏷️ Nom de fonction", code1: "calculer", code2: "calculate", code3: "calculate" },
                    { aspect: "🌐 Langue", code1: "Français", code2: "Mixte", code3: "Mixte" },
                    { aspect: "🛡️ Robustesse", code1: "⭐ Faible", code2: "⭐⭐ Moyenne", code3: "⭐⭐⭐ Élevée" },
                    { aspect: "📖 Clarté", code1: "Simple", code2: "Structuré", code3: "Professionnel" },
                    { aspect: "📏 PEP8", code1: "❌ Non", code2: "⚠️ Partiel", code3: "✅ Respecté" },
                    { aspect: "🚨 Gestion erreurs", code1: "Basique", code2: "Améliorée", code3: "Complète" }
                  ].map((row, index) => (
                    <tr key={index} className="hover:bg-slate-700/30 transition-colors">
                      <td className="p-3 font-medium">{row.aspect}</td>
                      <td className="p-3 text-center text-blue-200">{row.code1}</td>
                      <td className="p-3 text-center text-green-200">{row.code2}</td>
                      <td className="p-3 text-center text-yellow-200">{row.code3}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          {/* Principe Clé */}
          <div className="bg-gradient-to-r from-yellow-900/30 via-orange-900/30 to-red-900/30 backdrop-blur-sm rounded-2xl border border-yellow-500/20 p-8 mb-12">
            <div className="flex items-center gap-3 mb-6">
              <Lightbulb className="w-8 h-8 text-yellow-400" />
              <h3 className="text-2xl font-bold text-yellow-300">Principe Clé : La Spécificité</h3>
            </div>
            <div className="bg-yellow-500/10 border border-yellow-500/20 rounded-lg p-6 mb-6">
              <p className="text-lg text-yellow-200 font-semibold flex items-center gap-2">
                💡 <span>Insight Principal : Le principe ayant le plus d'impact est <strong>la spécificité</strong> du prompt.</span>
              </p>
            </div>
            
            <div className="grid md:grid-cols-2 gap-6">
              <div className="p-6 bg-red-500/10 border border-red-500/20 rounded-lg">
                <h4 className="font-bold text-red-300 mb-3 flex items-center gap-2">
                  🔄 Prompt Vague
                </h4>
                <p className="text-slate-300 text-sm mb-3">Code fonctionnel mais basique</p>
                <p className="text-red-300 text-sm">⏰ Faible initial + 🔄 Itérations</p>
              </div>
              <div className="p-6 bg-green-500/10 border border-green-500/20 rounded-lg">
                <h4 className="font-bold text-green-300 mb-3 flex items-center gap-2">
                  🎯 Prompt Spécifique
                </h4>
                <p className="text-slate-300 text-sm mb-3">Code robuste et documenté</p>
                <p className="text-green-300 text-sm">⏰ Plus long initial - 🎯 Moins d'effort après</p>
              </div>
            </div>
          </div>

          {/* Few-Shot Prompting */}
          <div className="bg-slate-800/50 backdrop-blur-sm rounded-2xl border border-slate-700/50 p-8">
            <h3 className="text-2xl font-bold mb-6 flex items-center gap-3">
              <Brain className="w-7 h-7 text-cyan-400" />
              Exercice 2.2 : Few-Shot Prompting
            </h3>
            
            <div className="grid lg:grid-cols-2 gap-8">
              <div>
                <h4 className="text-xl font-semibold mb-4 text-cyan-300">📈 Impact des Exemples</h4>
                <p className="text-slate-300 mb-4">L'ajout d'exemples a <strong>significativement amélioré</strong> :</p>
                <div className="space-y-3">
                  {[
                    { icon: "🎯", text: "Structure précise du format de sortie" },
                    { icon: "⚠️", text: "Gestion des valeurs invalides (longueur, caractères)" },
                    { icon: "🔄", text: "Cohérence dans la levée des erreurs" }
                  ].map((item, index) => (
                    <div key={index} className="flex items-center gap-3 p-3 bg-cyan-500/10 rounded-lg border border-cyan-500/20">
                      <span className="text-xl">{item.icon}</span>
                      <span className="text-slate-300">{item.text}</span>
                    </div>
                  ))}
                </div>
              </div>
              
              <div>
                <h4 className="text-xl font-semibold mb-4 text-pink-300">🎪 Quand utiliser le Few-Shot Prompting ?</h4>
                <div className="space-y-3">
                  {[
                    "📋 Formats très précis (codes produits, numéros de série)",
                    "🤔 Règles métier implicites ou ambiguës",
                    "🚨 Cas limites (ValueError, formats partiels)",
                    "📚 Scénarios multiples : bon/mauvais format, erreurs"
                  ].map((item, index) => (
                    <div key={index} className="p-3 bg-pink-500/10 rounded-lg border border-pink-500/20">
                      <span className="text-slate-300">{item}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            <div className="mt-8 p-6 bg-gradient-to-r from-red-900/30 to-orange-900/30 border border-red-500/20 rounded-lg">
              <h4 className="text-xl font-semibold mb-3 text-red-300 flex items-center gap-2">
                ⚖️ Limites des Exemples
              </h4>
              <p className="text-red-200 mb-3">🚨 Attention : Deux limites principales</p>
              <div className="grid md:grid-cols-2 gap-4">
                <div className="p-3 bg-red-500/10 rounded-lg">
                  <strong className="text-red-300">📉 Qualité :</strong>
                  <span className="text-slate-300"> Un mauvais exemple peut induire l'IA en erreur</span>
                </div>
                <div className="p-3 bg-red-500/10 rounded-lg">
                  <strong className="text-red-300">📊 Quantité :</strong>
                  <span className="text-slate-300"> Trop d'exemples = confusion. <strong>2-3 exemples bien choisis</strong> > 6 similaires</span>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Partie 3 */}
        <section className="mb-16">
          <div className="flex items-center gap-4 mb-8">
            <div className="w-16 h-16 rounded-full bg-gradient-to-r from-green-500 to-teal-500 flex items-center justify-center">
              <Wrench className="w-8 h-8 text-white" />
            </div>
            <h2 className="text-4xl font-bold">Partie 3 : Débogage et Amélioration</h2>
          </div>

          {/* Débogage Assisté */}
          <div className="bg-slate-800/50 backdrop-blur-sm rounded-2xl border border-slate-700/50 p-8 mb-12">
            <h3 className="text-2xl font-bold mb-6 flex items-center gap-3">
              <Bug className="w-7 h-7 text-red-400" />
              Exercice 3.1 : Débogage Assisté
            </h3>

            <div className="bg-red-900/30 border border-red-500/20 rounded-lg p-6 mb-8">
              <h4 className="text-xl font-semibold text-red-300 mb-4">🚨 Analyse d'Erreur</h4>
              <div className="bg-black/30 rounded-lg p-4 mb-4 font-mono text-red-200">
                TypeError: unsupported operand type(s) for +=: 'int' and 'str'
              </div>
              <div className="grid md:grid-cols-3 gap-4">
                <div className="p-3 bg-red-500/10 rounded-lg">
                  <strong className="text-red-300">Type :</strong>
                  <span className="text-slate-300"> TypeError</span>
                </div>
                <div className="p-3 bg-red-500/10 rounded-lg">
                  <strong className="text-red-300">Localisation :</strong>
                  <span className="text-slate-300"> Ligne `total += num`</span>
                </div>
                <div className="p-3 bg-red-500/10 rounded-lg">
                  <strong className="text-red-300">Cause :</strong>
                  <span className="text-slate-300"> Sommation d'un entier avec 'three' dans `[1, 2, 'three', 4]`</span>
                </div>
              </div>
            </div>

            <div className="grid lg:grid-cols-2 gap-8">
              <div>
                <h4 className="text-xl font-semibold mb-4 text-green-300">✅ Correctifs Appliqués</h4>
                <div className="space-y-3">
                  {[
                    { icon: "🔍", text: "Validation des types avant calcul" },
                    { icon: "🛡️", text: "Gestion listes vides (évitement DivisionByZero)" },
                    { icon: "💬", text: "Messages d'erreur contextualisés" },
                    { icon: "📚", text: "Documentation fonctionnelle ajoutée" }
                  ].map((item, index) => (
                    <div key={index} className="flex items-center gap-3 p-3 bg-green-500/10 rounded-lg border border-green-500/20">
                      <span className="text-xl">{item.icon}</span>
                      <span className="text-slate-300">{item.text}</span>
                    </div>
                  ))}
                </div>
              </div>

              <div>
                <h4 className="text-xl font-semibold mb-4 text-blue-300">🧪 Tests Unitaires avec Pytest</h4>
                <div className="space-y-4">
                  <div className="p-4 bg-blue-500/10 rounded-lg border border-blue-500/20">
                    <h5 className="font-semibold text-blue-300 mb-2">✅ Cas Nominaux</h5>
                    <ul className="text-sm text-slate-300 space-y-1">
                      <li>• Listes homogènes (entiers/décimaux)</li>
                      <li>• Listes mixtes (entiers + décimaux)</li>
                      <li>• Singleton numérique</li>
                    </ul>
                  </div>
                  <div className="p-4 bg-yellow-500/10 rounded-lg border border-yellow-500/20">
                    <h5 className="font-semibold text-yellow-300 mb-2">❌ Cas d'Erreur</h5>
                    <ul className="text-sm text-slate-300 space-y-1">
                      <li>• Liste vide</li>
                      <li>• Éléments non numériques</li>
                      <li>• Valeurs None</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Refactoring Assisté */}
          <div className="bg-slate-800/50 backdrop-blur-sm rounded-2xl border border-slate-700/50 p-8 mb-12">
            <h3 className="text-2xl font-bold mb-6 flex items-center gap-3">
              <RefreshCw className="w-7 h-7 text-purple-400" />
              Exercice 3.2 : Refactoring Assisté
            </h3>

            <div className="mb-8">
              <h4 className="text-xl font-semibold mb-4 text-purple-300">📊 Analyse du Code Initial</h4>
              <div className="overflow-x-auto">
                <table className="w-full text-sm">
                  <thead>
                    <tr className="border-b border-slate-600">
                      <th className="text-left p-3 font-semibold text-purple-300">Problématique</th>
                      <th className="text-center p-3 font-semibold text-blue-300">Impact</th>
                      <th className="text-center p-3 font-semibold text-yellow-300">Priorité</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-700">
                    {[
                      { problem: "Variables obscures", impact: "📉 Lisibilité", priority: "🔴 Haute" },
                      { problem: "Code monolithique", impact: "🔧 Maintenabilité", priority: "🔴 Haute" },
                      { problem: "Absence documentation", impact: "📚 Compréhension", priority: "🟡 Moyenne" },
                      { problem: "Pas de validation", impact: "🛡️ Robustesse", priority: "🟡 Moyenne" }
                    ].map((row, index) => (
                      <tr key={index} className="hover:bg-slate-700/30 transition-colors">
                        <td className="p-3 font-medium">{row.problem}</td>
                        <td className="p-3 text-center text-blue-200">{row.impact}</td>
                        <td className="p-3 text-center text-yellow-200">{row.priority}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            <div className="bg-gradient-to-r from-green-900/30 to-teal-900/30 border border-green-500/20 rounded-lg p-6">
              <h4 className="text-xl font-semibold mb-4 text-green-300">🏆 Résultats du Refactoring</h4>
              <div className="grid md:grid-cols-2 gap-4">
                {[
                  { icon: "🔧", text: "Encapsulation dans une fonction nommée (bubble_sort)" },
                  { icon: "📏", text: "Respect des conventions PEP8" },
                  { icon: "📚", text: "Introduction de docstrings structurées" },
                  { icon: "🏷️", text: "Renommage pour améliorer la clarté (array, index)" },
                  { icon: "📦", text: 'Ajout du bloc if __name__ == "__main__":' }
                ].map((item, index) => (
                  <div key={index} className="flex items-start gap-3 p-3 bg-green-500/10 rounded-lg">
                    <span className="text-xl flex-shrink-0">{item.icon}</span>
                    <span className="text-slate-300 text-sm">{item.text}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Documentation Automatisée */}
          <div className="bg-slate-800/50 backdrop-blur-sm rounded-2xl border border-slate-700/50 p-8">
            <h3 className="text-2xl font-bold mb-6 flex items-center gap-3">
              <FileText className="w-7 h-7 text-cyan-400" />
              Exercice 3.3 : Documentation Automatisée
            </h3>

            <div className="bg-cyan-900/30 border border-cyan-500/20 rounded-lg p-6 mb-6">
              <h4 className="text-xl font-semibold text-cyan-300 mb-4">🧠 Fonction Générée : get_user_permissions
