import Link from "next/link";

export default function NotFound() {
	return (
		<div className="w-screen h-screen relative flex items-center justify-center overflow-hidden bg-green-700">
			<div className="absolute inset-0 opacity-20">
				<div className="w-full h-full border-4 border-white"></div>
				<div className="absolute left-1/2 top-0 bottom-0 w-1 bg-white -translate-x-1/2"></div>
				<div className="absolute top-1/2 left-1/2 w-64 h-64 border-4 border-white rounded-full -translate-x-1/2 -translate-y-1/2"></div>
			</div>

			<h1 className="text-white font-black text-[30vw] leading-none select-none tracking-tighter drop-shadow-2xl z-10">
				404
			</h1>

			<div className="absolute bottom-10 text-center text-white/90 z-10">
				<p className="text-xl font-semibold">⚽ Offside!</p>
				<p className="text-sm opacity-80">Táto stránka sa nedostala cez obranu.</p>
			</div>
			<Link
				href="/"
				className="absolute bottom-10 z-10 px-6 py-3 bg-white text-green-800 font-bold rounded-full shadow-lg hover:bg-gray-200 transition"
			>
				🏠 Domov
			</Link>

			<div className="absolute animate-bounce top-10 right-10 text-5xl">⚽</div>
		</div>
	);
}
