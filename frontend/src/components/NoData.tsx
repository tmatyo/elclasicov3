import { refresh } from "@/src/actions/refresh";

export default function NoData() {
	return (
		<div className="w-full flex flex-col items-center justify-center py-20 text-center">
			<div className="text-5xl mb-4">⚠️</div>
			<h2 className="text-2xl font-bold text-gray-800">Niečo sa pokazilo</h2>
			<p className="mt-2 text-gray-500 max-w-md">Žiadne dáta k dispozícii. Skúste to znova neskôr.</p>
			<form action={refresh}>
				<button className="mt-6 px-5 py-2 bg-black text-white rounded-full hover:bg-gray-800 transition cursor-pointer">
					Skúsiť znova
				</button>
			</form>
		</div>
	);
}
